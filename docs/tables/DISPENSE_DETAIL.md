# DISPENSE_DETAIL

> Table to store additional dispensing details when the fill process is done externally; via a mail order pharmacy.

**Description:** Dispense Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DETAIL_GROUP_SEQ` | DOUBLE | NOT NULL |  | The sequence used to group related dispense detail. |
| 2 | `DETAIL_TYPE_CD` | DOUBLE | NOT NULL |  | The type of dispense detail recorded in this row. |
| 3 | `DETAIL_VALUE_CD` | DOUBLE | NOT NULL |  | The value of the dispense detail if a numerif or coded value. |
| 4 | `DETAIL_VALUE_DT_TM` | DATETIME |  |  | The date and time value of the dispense detail if of type date/time. |
| 5 | `DETAIL_VALUE_NBR` | DOUBLE |  |  | The value of the dispense detail if a numerif or coded value. |
| 6 | `DETAIL_VALUE_TM_ZN` | DOUBLE |  |  | The time zone associated with the corresponding DT_TM column. |
| 7 | `DETAIL_VALUE_TXT` | VARCHAR(500) |  |  | The display value of the dispense detail. |
| 8 | `DISPENSE_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the DISPENSE_DETAIL table. |
| 9 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for a dispense event. |
| 10 | `DISPENSE_STATUS_CD` | DOUBLE | NOT NULL |  | The dispense status code which represents the dispense tracking step during which the dispense detail was obtained. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |

