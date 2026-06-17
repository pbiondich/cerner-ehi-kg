# PCS_QC_FILTER

> This table contains the filter templates for PathNet Common Services

**Description:** PathNet Common Services Quality Control Filter  
**Table type:** REFERENCE  
**Primary key:** `FILTER_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPLAY_SEQ_NBR` | DOUBLE | NOT NULL |  | The order in which the filters were added to this template or filter set. |
| 2 | `FILTER_CD` | DOUBLE | NOT NULL |  | This is the filter the user has chosen to associate with this filter set number. |
| 3 | `FILTER_ID` | DOUBLE | NOT NULL | PK | ID which makes each PCS_QC_FILTER row unique. |
| 4 | `FILTER_SET_NBR` | DOUBLE | NOT NULL |  | This is the filter set number for the chosen template this row is associated with. |
| 5 | `TEMPLATE_CD` | DOUBLE | NOT NULL |  | This references back to the code value table to determine which template this row is associated with. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PCS_QC_FILTER_DEFAULT](PCS_QC_FILTER_DEFAULT.md) | `FILTER_ID` |

