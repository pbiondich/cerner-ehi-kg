# BB_QC_REL_REAGENT_DETAIL

> This table maintains a list of reagent relationships that can be used in a quality control group.

**Description:** Blood Bank Quality Control Related Reagent  
**Table type:** REFERENCE  
**Primary key:** `RELATED_REAGENT_DETAIL_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONTROL_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the control reagent. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `ENHANCEMENT_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the enhancement reagent. |
| 6 | `PHASE_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the phase used during the QC testing. |
| 7 | `PREV_RELATED_REAGENT_DETAIL_ID` | DOUBLE | NOT NULL |  | This field contains the unique ID of the previous version of the current row. |
| 8 | `RELATED_REAGENT_DETAIL_ID` | DOUBLE | NOT NULL | PK | This field uniquely identifies the reagent relationship detail. |
| 9 | `RELATED_REAGENT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the parent reagent. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RELATED_REAGENT_ID` | [BB_QC_REL_REAGENT](BB_QC_REL_REAGENT.md) | `RELATED_REAGENT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BB_QC_EXPECTED_RESULT_R](BB_QC_EXPECTED_RESULT_R.md) | `RELATED_REAGENT_DETAIL_ID` |

