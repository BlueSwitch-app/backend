import datetime
def CalculateCO2(devices):
    CO2Total = 0
    device_CO2 = {}  # CO2 por dispositivo
    device_emails = {}  # Email por dispositivo

    for device in devices:
        device_name = device.get("nombre", "Desconocido")
        device_email = device.get("email", "Desconocido")
        device_CO2[device_name] = 0
        device_emails[device_name] = device_email

        created_at_list = device.get("created_at", [])
        if isinstance(created_at_list, list):
            for interval in created_at_list:
                if isinstance(interval, list) and len(interval) == 2:
                    start, end = interval
                    try:
                        # start
                        if start:
                            start_datetime = datetime.datetime.fromisoformat(str(start))
                            if start_datetime.tzinfo is None:
                                start_datetime = start_datetime.replace(tzinfo=datetime.timezone.utc)
                        else:
                            continue
                        # end
                        if end:
                            end_datetime = datetime.datetime.fromisoformat(str(end))
                            if end_datetime.tzinfo is None:
                                end_datetime = end_datetime.replace(tzinfo=datetime.timezone.utc)
                        else:
                            end_datetime = datetime.datetime.now(datetime.timezone.utc)

                        hours = (end_datetime - start_datetime).total_seconds() / 3600
                        watts = device.get("watts", 0)
                        CO2 = (watts * hours / 1000) * 0.44
                        CO2Total += CO2
                        device_CO2[device_name] += CO2

                    except Exception as e:
                        print(f"Error procesando intervalo {interval}: {e}")

    # Obtener dispositivo con más CO2
    if device_CO2:
        max_device_name = max(device_CO2, key=device_CO2.get)
        max_device_email = device_emails.get(max_device_name, None)
    else:
        max_device_name = None
        max_device_email = None

    total_CO2 = round(CO2Total, 3) if CO2Total > 0 else (1 if CO2Total < 0 else 0)
    return total_CO2, {"nombre": max_device_name, "email": max_device_email}