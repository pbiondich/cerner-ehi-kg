# RCM_CLARIFICATION

> Stores Clarificaiton for the Care Management Solution

**Description:** RevWorks Care Management - Clarification  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CLARIFICATION_CODE` | VARCHAR(50) | NOT NULL |  | The J A Thomas code Identifier |
| 4 | `CLARIFICATION_IDENT` | VARCHAR(50) | NOT NULL |  | The unique J A Thomas clarification identifier. |
| 5 | `CLARIFICATION_RESP_CD` | DOUBLE | NOT NULL |  | The code describing the responses of clarification |
| 6 | `CLARIFICATION_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of clarification. |
| 7 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the clarification was created. |
| 8 | `DOCUMENT_REVIEW_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the rcm_doc_review row containing the clarification. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the long_text row containing the clarification text. |
| 11 | `PREV_RCM_CLARIFICATION_ID` | DOUBLE | NOT NULL |  | Used to track versions of the clarification information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 12 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the personnel group for this clarification. |
| 13 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The physician personnel of the clarification. |
| 14 | `RCM_CLARIFICATION_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a clarification for the Care Management solution. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOCUMENT_REVIEW_ID` | [RCM_DOC_REVIEW](RCM_DOC_REVIEW.md) | `RCM_DOC_REVIEW_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

