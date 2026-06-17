# DISPENSE_STATUS

> Dispense_Status

**Description:** Dispense Status  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | DISPENSE_HX_ID |
| 2 | `DISPENSE_STATUS_CD` | DOUBLE | NOT NULL |  | dispense status code |
| 3 | `DISPENSE_STATUS_ID` | DOUBLE | NOT NULL |  | dispense_status_id |
| 4 | `LEVEL5_CD` | DOUBLE | NOT NULL |  | LEVEL5 CD |
| 5 | `SUBSECTION_CD` | DOUBLE | NOT NULL |  | subsection_cd |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |

