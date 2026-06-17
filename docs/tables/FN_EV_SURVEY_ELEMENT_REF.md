# FN_EV_SURVEY_ELEMENT_REF

> Stores the layout reference data of a given survey used by Emergent Event.

**Description:** FN_EV_SURVEY_ELEMENT_REF  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ELEMENT_NAME` | VARCHAR(255) |  |  | Indicates name of element that is displayed to the user. |
| 2 | `ELEMENT_SEQ` | DOUBLE |  |  | Indicates sequence of elements in the survey. |
| 3 | `EVENT_CD` | DOUBLE |  |  | Documented Result for a Question type. Foreign key to CODE_VALUE table |
| 4 | `FN_EV_SURVEY_DETAIL_REF_ID` | DOUBLE |  | FK→ | Identifies the survey detail ID of the survey whic contais this element |
| 5 | `FN_EV_SURVEY_ELEMENT_REF_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `HIDE_IND` | DOUBLE |  |  | Indicates item is hidden and not displayed to the user in the survey |
| 7 | `LINK_EVENT_CD` | DOUBLE |  |  | Event Code linked to associated nomenclature for documentation. |
| 8 | `NOMENCLATURE_ID` | DOUBLE |  | FK→ | Stores nomenclature id that is associated to parent element. |
| 9 | `TYPE_FLAG` | DOUBLE |  |  | Indicates if the element is a SECTION or QUESTION |
| 10 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FN_EV_SURVEY_DETAIL_REF_ID` | [FN_EV_SURVEY_DETAIL_REF](FN_EV_SURVEY_DETAIL_REF.md) | `FN_EV_SURVEY_DETAIL_REF_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

