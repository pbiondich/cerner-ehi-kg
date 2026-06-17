# BB_QC_EXPECTED_RESULT_R

> This field maintains a list of expected results for a specific QC group relationship.

**Description:** Blood Bank Quality Control Expected Result  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `EXPECTED_RESULT_ID` | DOUBLE | NOT NULL |  | This field uniquely identifies the expected result row. |
| 5 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the expected result (Nomenclature) |
| 6 | `PREV_EXPECTED_RESULT_ID` | DOUBLE | NOT NULL |  | This field contains the unique id of the previous version of the current row. |
| 7 | `RELATED_REAGENT_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | This field links the expected result with a specific group relationship row (BB_QC_REL_REAGENT_DETAIL) |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `RELATED_REAGENT_DETAIL_ID` | [BB_QC_REL_REAGENT_DETAIL](BB_QC_REL_REAGENT_DETAIL.md) | `RELATED_REAGENT_DETAIL_ID` |

