# PO_BATCH

> This is a holding table for outbound purchase orders.

**Description:** PO Batch  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was inserted. |
| 3 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 4 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 5 | `PO_BATCH_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 6 | `TRANSMIT_DT_TM` | DATETIME |  |  | Transmit Date and Time |
| 7 | `TRANSMIT_FLAG` | DOUBLE |  |  | Transmit Flag is used to recognize whether the po's are transmitted or not. |
| 8 | `TRANSMIT_STATUS_CD` | DOUBLE |  |  | Transmit_Status_CD |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VENDOR_CD` | DOUBLE | NOT NULL |  | The vendor for which this batch was created. |
| 15 | `VENDOR_SITE_ID` | DOUBLE | NOT NULL | FK→ | The vendor account. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `VENDOR_SITE_ID` | [VENDOR_SITE](VENDOR_SITE.md) | `VENDOR_SITE_ID` |

