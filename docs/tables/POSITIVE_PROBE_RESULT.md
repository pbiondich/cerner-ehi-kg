# POSITIVE_PROBE_RESULT

> Indicates whether a positive reaction occured for a specific probe number in an HLA molecular typing blot.

**Description:** Positive Probe Result  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL |  | Identifies the inventory lot of the Molecular Blot being used to arrive at the results. It is a foreign key reference to the primary key of the lot_number_info table. |
| 2 | `ORDER_ID` | DOUBLE | NOT NULL |  | Relates results for the Molecular Blot to a specific order. It is a foreign key reference to the primary key of the orders table. |
| 3 | `PROBE_NUMBER` | DOUBLE | NOT NULL |  | Number of the molecular blot probe which had a positive reaction. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

