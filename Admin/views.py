from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal, InvalidOperation

from .models import Service


def add_service(request):
    """Render add_service page; handle POST to create a Service (PRG).

    Expects form fields: name, description, price (optional), active (checkbox).
    """
    if request.method == 'POST':
        # CREATE: Extract form data from POST request
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()
        price_raw = request.POST.get('price', '').strip()
        active = bool(request.POST.get('active'))

        # Safely parse price as Decimal
        price = None
        if price_raw:
            try:
                price = Decimal(price_raw)
            except (InvalidOperation, ValueError):
                price = None

        # Create Service if name is provided
        if name:
            Service.objects.create(
                name=name,
                description=description,
                price=price,
                active=active,
            )

        # Redirect to avoid form re-submission (PRG pattern)
        return redirect('add_service')

    # READ: Fetch all services for display
    services = Service.objects.all()
    return render(request, 'add_service.html', {'services': services})


def delete_service(request, pk: int):
    """Delete a service by primary key. Only accepts POST."""
    if request.method != 'POST':
        return redirect('add_service')

    # DELETE: Retrieve service by ID and remove it
    svc = get_object_or_404(Service, pk=pk)
    svc.delete()
    # Redirect back to the services list
    return redirect('add_service')
