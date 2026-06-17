# PCS_QC_FILTER_DEFAULT

> Contains PathNet Common Services QC Template Filter Defaults

**Description:** PathNet Common Services Quality Control Filter Default  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FILTER_DEFAULT_ID` | DOUBLE | NOT NULL |  | Identifier which makes each row in PCS_QC_FILTER_DEFAULT unique. |
| 2 | `FILTER_DEFAULT_SEQ_NBR` | DOUBLE | NOT NULL |  | Keeps each row on the table unique. |
| 3 | `FILTER_ID` | DOUBLE | NOT NULL | FK→ | Provides a reference back to the row on the PCS_QC_FILTER table. |
| 4 | `FILTER_NBR` | DOUBLE | NOT NULL |  | Stores the numeric value for the filter selected. i.e. This value will be equal to the number of days when the "number of days prior to date" filter has been selected. |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Sores the value for the filter selected. This value will hold either a control_id, code_value, lot_type or zero. |
| 6 | `PARENT_ENTITY_NAME` | CHAR(30) | NOT NULL |  | Name of the table that this row references. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FILTER_ID` | [PCS_QC_FILTER](PCS_QC_FILTER.md) | `FILTER_ID` |

