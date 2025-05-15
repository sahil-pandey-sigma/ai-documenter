# Tutorial: sisforce-pig_backend-a449e3c497d4

This project is a *backend API* for an **investment management platform**.
It allows users like *investors* and *admins* to manage their accounts, track **portfolio companies**
and their funding rounds, and oversee the entire **investment deal lifecycle**, including digital
agreement signing. The system also provides dashboards with key financial metrics and utilizes
services like DocuSign for agreements and S3 for file storage.


**Source Repository:** [None](None)

```mermaid
flowchart TD
    A0["Django Models (ORM)
"]
    A1["API Views and URL Routing
"]
    A2["Data Serializers
"]
    A3["User Management & Authentication
"]
    A4["Deal Lifecycle Management
"]
    A5["Portfolio Company Management
"]
    A6["Utility Services & Helpers
"]
    A1 -- "Accesses data via" --> A0
    A1 -- "Processes I/O with" --> A2
    A2 -- "Maps data for" --> A0
    A3 -- "Stores user data using" --> A0
    A1 -- "Exposes functionality of" --> A3
    A3 -- "Uses for user data (de)seri..." --> A2
    A3 -- "Sends emails via" --> A6
    A4 -- "Stores deal data using" --> A0
    A1 -- "Exposes functionality of" --> A4
    A4 -- "Uses for deal data (de)seri..." --> A2
    A4 -- "Manages documents using" --> A6
    A5 -- "Stores company data using" --> A0
    A1 -- "Exposes functionality of" --> A5
    A5 -- "Uses for company data (de)s..." --> A2
    A5 -- "Sends notifications via" --> A6
    A4 -- "Links deals to" --> A5
```

## Chapters

1. [Django Models (ORM)
](01_django_models__orm__.md)
2. [User Management & Authentication
](02_user_management___authentication_.md)
3. [Portfolio Company Management
](03_portfolio_company_management_.md)
4. [Deal Lifecycle Management
](04_deal_lifecycle_management_.md)
5. [Data Serializers
](05_data_serializers_.md)
6. [API Views and URL Routing
](06_api_views_and_url_routing_.md)
7. [Utility Services & Helpers
](07_utility_services___helpers_.md)
