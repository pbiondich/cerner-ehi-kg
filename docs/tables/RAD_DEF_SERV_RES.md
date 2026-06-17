# RAD_DEF_SERV_RES

> The Rad_Def_Serv_Res table contains default locations for other service resources. (ex. folder check-in location for a library group)

**Description:** Rad Default Service Resources  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEF_SER_RES_CD` | DOUBLE | NOT NULL | FK→ | The Def_Ser_Res_Cd is a foreign key to the Service_Resource table. This identifies a service resource that is used for a specific purpose by another location. |
| 2 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The Service_Resource_Cd identifies a service resource that is having a default location set up. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `USAGE_CD` | DOUBLE | NOT NULL |  | The Usage_Cd identifies what the default location is used for by the service resource. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEF_SER_RES_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

