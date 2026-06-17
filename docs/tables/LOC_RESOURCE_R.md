# LOC_RESOURCE_R

> Indicates which locations a service resource can perform work for.

**Description:** Location Service Resource Relationship  
**Table type:** REFERENCE  
**Primary key:** `LOCATION_CD`, `LOC_RESOURCE_TYPE_CD`, `SEQUENCE`, `SERVICE_RESOURCE_CD`  
**Columns:** 11  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GROUP_SEQUENCE` | DOUBLE |  |  | Used to reconstruct the user interface for building and maintaining calendars. The user can create multiple calendar scenarios for a resource. The group sequence is used to keep all of the data rows together for a given scenario |
| 2 | `LOCATION_CD` | DOUBLE | NOT NULL | PK FK→ | The location which is being serviced by the resource. |
| 3 | `LOC_RESOURCE_TYPE_CD` | DOUBLE | NOT NULL | PK | The product or discipline associated with the relationship. Examples include Lab, Rad, etc. |
| 4 | `MM_VENDOR_CUSTOMER_ACCOUNT_ID` | DOUBLE | NOT NULL |  | The Vendor's (service resource) customer account associated with the service relationship. Materials Management |
| 5 | `SEQUENCE` | DOUBLE | NOT NULL | PK | Sequence. Used to differentiate rows with the same resource and service area location. The user may create more than one calendar row with the same service area (may make the priorities, dow, time of day, etc. different but the service area is the same). |
| 6 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | PK FK→ | The service resource which is providing service to the location. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [LOC_RESOURCE_CALENDAR](LOC_RESOURCE_CALENDAR.md) | `LOCATION_CD` |
| [LOC_RESOURCE_CALENDAR](LOC_RESOURCE_CALENDAR.md) | `LOC_RESOURCE_TYPE_CD` |
| [LOC_RESOURCE_CALENDAR](LOC_RESOURCE_CALENDAR.md) | `SEQUENCE` |
| [LOC_RESOURCE_CALENDAR](LOC_RESOURCE_CALENDAR.md) | `SERVICE_RESOURCE_CD` |

