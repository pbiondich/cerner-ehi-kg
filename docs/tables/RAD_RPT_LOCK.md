# RAD_RPT_LOCK

> The Rad_Rpt_Lock table is an extension of the order_radiology table. It shows which orders have been locked in order to modify the associated report.

**Description:** Rad Report Lock  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOCK_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of lock being held. A 1 indicates a Radiologist Hold on a report to be completed later. A 0 indicates a Regular lock of report that could occur by application access of the report. |
| 2 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key to the order_radiology table. This table may not contain all of the order_id's on the order_radiology table. |
| 3 | `PS_RPT_LOCK_IND` | DOUBLE | NOT NULL |  | Indicates that the report is currently being dictated by PowerScribe. |
| 4 | `RPT_LOCK_DT_TM` | DATETIME |  |  | This is the date and time that the report lock was created. |
| 5 | `RPT_LOCK_ID` | DOUBLE | NOT NULL | FK→ | The rpt_lock_id is the person id of the personnel that has the report locked. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `ORDER_ID` |
| `RPT_LOCK_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

