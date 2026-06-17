# PRIVILEGE_EXCEPTION

> This table contains inclusions or exclusioins to privileges defined.

**Description:** PRIVILEGE EXCEPTION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `EVENT_SET_NAME` | VARCHAR(100) |  |  | Event set name of the event code |
| 6 | `EXCEPTION_ENTITY_NAME` | VARCHAR(40) |  |  | The name of the table that the exception row is from. |
| 7 | `EXCEPTION_ID` | DOUBLE | NOT NULL |  | Contains a pointer to the database that this exception pertains to. It could contain an order_catalog_cd, a task_assay_cd, etc. |
| 8 | `EXCEPTION_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates which database this exception relates to. Could be the order catalog, an event set, etc. |
| 9 | `PRIVILEGE_EXCEPTION_ID` | DOUBLE | NOT NULL |  | The unique identifier of a row on this table. |
| 10 | `PRIVILEGE_ID` | DOUBLE | NOT NULL | FK→ | The primary index of the privilege that this exception is tied to. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRIVILEGE_ID` | [PRIVILEGE](PRIVILEGE.md) | `PRIVILEGE_ID` |

