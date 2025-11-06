#!/bin/bash

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to validate Docker and Docker Compose availability
validate_prerequisites() {
    print_status "Validating prerequisites..."

    if ! command_exists docker; then
        print_error "Docker is not installed or not in PATH"
        exit 1
    fi

    if ! command_exists docker-compose && ! docker compose version >/dev/null 2>&1; then
        print_error "Docker Compose is not installed or not in PATH"
        exit 1
    fi

    print_success "Prerequisites validated"
}

# Function to run docker compose up
start_services() {
    print_status "Starting Docker Compose services..."

    if command_exists docker-compose; then
        docker-compose up -d
    else
        docker compose up -d
    fi

    print_success "Services started"
}

# Function to wait for container health
wait_for_health() {
    print_status "Waiting for ai-counsel container to be healthy..."

    local max_attempts=30
    local attempt=1

    while [ $attempt -le $max_attempts ]; do
        if [ "$(docker ps --filter "name=ai-counsel" --filter "health=healthy" --format "{{.Names}}")" = "dev-deploy-ai-counsel-1" ]; then
            print_success "Container is healthy"
            return 0
        fi

        print_status "Attempt $attempt/$max_attempts: Container not yet healthy, waiting..."
        sleep 10
        ((attempt++))
    done

    print_error "Container failed to become healthy within $(($max_attempts * 10)) seconds"
    return 1
}

# Function to verify health endpoint
verify_health() {
    print_status "Verifying health endpoint..."

    local health_url="http://localhost:9090/health"
    local max_attempts=10
    local attempt=1

    while [ $attempt -le $max_attempts ]; do
        if curl -f -s "$health_url" >/dev/null 2>&1; then
            print_success "Health endpoint is responding"

            # Print health response
            echo "Health check response:"
            curl -s "$health_url" | jq . 2>/dev/null || curl -s "$health_url"

            return 0
        fi

        print_status "Attempt $attempt/$max_attempts: Health endpoint not responding, waiting..."
        sleep 5
        ((attempt++))
    done

    print_error "Health endpoint failed to respond within $(($max_attempts * 5)) seconds"
    return 1
}

# Function to show service status
show_status() {
    print_status "Service status:"
    if command_exists docker-compose; then
        docker-compose ps
    else
        docker compose ps
    fi
}

# Function to show logs
show_logs() {
    print_status "Recent container logs:"
    docker logs --tail 20 dev-deploy-ai-counsel-1 2>/dev/null || print_warning "Could not retrieve logs"
}

# Function to print URLs
print_urls() {
    echo ""
    print_success "Services are running!"
    echo "Health check: http://localhost:9090/health"
    echo "Metrics: http://localhost:9090/metrics"
    echo "API: http://localhost:8000"
}

# Function to verify stack
verify() {
    print_status "Running verification process..."

    # Build images
    print_status "Building Docker images..."
    if command_exists docker-compose; then
        docker-compose build
    else
        docker compose build
    fi

    # Start services
    start_services

    # Wait for health
    wait_for_health

    # Verify health endpoint
    verify_health

    # Show status
    show_status

    # Print URLs
    print_urls

    print_success "Verification complete!"
}

# Main execution
main() {
    case "${1:-}" in
        "verify")
            validate_prerequisites
            verify
            ;;
        "restart")
            print_status "Restarting services..."
            if command_exists docker-compose; then
                docker-compose restart
            else
                docker compose restart
            fi
            wait_for_health
            verify_health
            show_status
            print_urls
            ;;
        *)
            validate_prerequisites
            start_services
            wait_for_health
            show_logs
            verify_health
            show_status
            print_urls
            ;;
    esac
}

main "$@"