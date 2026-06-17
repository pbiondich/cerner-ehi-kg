# SEC_RES_OPER_PRIN_R

> This table will principals associated to the SEC_RESOURCE_OPER

**Description:** Security resource operations principal relationships  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESS_TYPE_NBR` | DOUBLE | NOT NULL |  | The access specifier for the row. Current values are 1 - allow, 2 - disallow. In the future other access types may be possible. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `SEC_PRINCIPAL_ID` | DOUBLE | NOT NULL | FK→ | The primary key of the principal that this row specifies the resource operations. |
| 7 | `SEC_RES_OPERATIONS_ID` | DOUBLE | NOT NULL | FK→ | The primary key of the resource operation |
| 8 | `SEC_RES_OPER_PRIN_R_ID` | DOUBLE | NOT NULL |  | The primary key identifying the resource Operations for the principal. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SEC_PRINCIPAL_ID` | [SEC_PRINCIPAL](SEC_PRINCIPAL.md) | `SEC_PRINCIPAL_ID` |
| `SEC_RES_OPERATIONS_ID` | [SEC_RES_OPERATIONS](SEC_RES_OPERATIONS.md) | `SEC_RES_OPERATIONS_ID` |

