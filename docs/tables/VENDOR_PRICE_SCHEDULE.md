# VENDOR_PRICE_SCHEDULE

> Vendor Price Schedule table

**Description:** Vendor Price Schedule  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | Application which created this row |
| 6 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date/time this entry was created. |
| 7 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 8 | `CREATE_TASK` | DOUBLE | NOT NULL |  | Task which created this row |
| 9 | `DESCRIPTION` | VARCHAR(100) |  |  | Description of price schedule |
| 10 | `PRICE_SCHEDULE_TYPE_CD` | DOUBLE | NOT NULL |  | Price Schedule type code value |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `VENDOR_CD` | DOUBLE | NOT NULL |  | Vendor associated with this account |
| 17 | `VENDOR_PRICE_SCHEDULE_ID` | DOUBLE | NOT NULL |  | Primary key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

