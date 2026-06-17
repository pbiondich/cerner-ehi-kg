# OUTCOME_ACTIVITY

> Used to hold definition for outcomes as they are ordered

**Description:** Outcome activity table  
**Table type:** ACTIVITY  
**Primary key:** `OUTCOME_ACTIVITY_ID`  
**Columns:** 40  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENT_ID` | DOUBLE | NOT NULL | FK→ | Outcome comment id. This is foreign key to LONG_TEXT table. |
| 2 | `DESCRIPTION` | VARCHAR(100) | NOT NULL |  | Description for a particular outcome |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 4 | `END_DT_TM` | DATETIME |  |  | Used to define a date range for results that are queried when evaluating the outcome |
| 5 | `END_ESTIMATED_IND` | DOUBLE | NOT NULL |  | To indicate whether the outcome end date time is estimated or precise. |
| 6 | `END_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 7 | `EVENT_CD` | DOUBLE | NOT NULL | FK→ | Event code from v500_event_code which is used to identify relevant results |
| 8 | `EXPAND_QTY` | DOUBLE |  |  | Range value to be used to set the limit of evaluating the outcomes past their target |
| 9 | `EXPAND_UNIT_CD` | DOUBLE | NOT NULL |  | Unit code to be used together with the range value to set the limit of evaluating the outcomes past their target |
| 10 | `EXPECTATION` | VARCHAR(200) | NOT NULL |  | Expected value for the outcome formatted from the outcome criteria built by the users |
| 11 | `GROUP_COLLABORATION_IND` | DOUBLE | NOT NULL |  | Indicates if the outcome is a team outcome or individual outcome. |
| 12 | `HIDE_EXPECTATION_IND` | DOUBLE | NOT NULL |  | Used to suppress the display of outcome expectation string in the front end application. |
| 13 | `NOMEN_STRING_FLAG` | DOUBLE | NOT NULL |  | Identifies which nomenclature table field will be used to display the alpha response. 0 - Short String 1 - Mnemonic 2 - Source String |
| 14 | `OPERAND_MEAN` | CHAR(12) |  |  | Meaning that defines the operand when multiple alpha responses are used to define an outcome (AND or OR) |
| 15 | `OUTCOME_ACTIVITY_ID` | DOUBLE | NOT NULL | PK | Unique identifier for a particular outcome instance |
| 16 | `OUTCOME_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for a particular outcome from OUTCOME_CATALOG table |
| 17 | `OUTCOME_CLASS_CD` | DOUBLE | NOT NULL |  | Outcome class codeColumn |
| 18 | `OUTCOME_STATUS_CD` | DOUBLE | NOT NULL |  | Outcome status identifier |
| 19 | `OUTCOME_STATUS_DT_TM` | DATETIME | NOT NULL |  | Date & time value indicating when an outcome reached its current status |
| 20 | `OUTCOME_STATUS_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 21 | `OUTCOME_TYPE_CD` | DOUBLE | NOT NULL |  | Outcome Type Code - Outcome type identifier |
| 22 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 23 | `PRIORITY_NBR` | DOUBLE | NOT NULL |  | Defines the priority of the outcome activity. 0 if no priority is assigned. |
| 24 | `REFERENCE_TASK_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for a task that is used to chart values for the outcome. |
| 25 | `REF_TEXT_RELTN_ID` | DOUBLE | NOT NULL |  | Unique identifier used to link outcome definition to the appropriate version of reference text defined for the outcome. |
| 26 | `RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | Format type of the result value which is used to evaluate the outcome |
| 27 | `SINGLE_SELECT_IND` | DOUBLE | NOT NULL |  | Used in conjunction with multi-criteria outcomes to indicate that only a single value can be selected when charting results against this outcome in Document In Plan view. |
| 28 | `SOURCE_FLAG` | DOUBLE | NOT NULL |  | Where the outcome was written from; 0: PowerPlans, 1: BodySystems MPage, 2: Goals MPage Component |
| 29 | `START_DT_TM` | DATETIME |  |  | Used to define a date range for results that are queried when evaluating the outcome |
| 30 | `START_ESTIMATED_IND` | DOUBLE | NOT NULL |  | To indicate whether the outcome start is estimated or precise. |
| 31 | `START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 32 | `TARGET_DURATION_QTY` | DOUBLE |  |  | Target duration quantity as defined by plan reference catalog |
| 33 | `TARGET_DURATION_UNIT_CD` | DOUBLE | NOT NULL |  | Target duration unit code as defined by plan reference catalog |
| 34 | `TARGET_TYPE_CD` | DOUBLE | NOT NULL |  | Target type codeColumn |
| 35 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | DTA from discrete_task_assay table which is used to identify an event_cd and criteria values for the outcome definition |
| 36 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 37 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 38 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 39 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 40 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `EVENT_CD` | [V500_EVENT_CODE](V500_EVENT_CODE.md) | `EVENT_CD` |
| `OUTCOME_CATALOG_ID` | [OUTCOME_CATALOG](OUTCOME_CATALOG.md) | `OUTCOME_CATALOG_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REFERENCE_TASK_ID` | [ORDER_TASK](ORDER_TASK.md) | `REFERENCE_TASK_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [OUTCOME_ACTION](OUTCOME_ACTION.md) | `OUTCOME_ACTIVITY_ID` |
| [OUTCOME_ACTIVITY_DETAIL](OUTCOME_ACTIVITY_DETAIL.md) | `OUTCOME_ACTIVITY_ID` |
| [OUTCOME_ACTIVITY_RELTN](OUTCOME_ACTIVITY_RELTN.md) | `CHILD_OUTCOME_ACTIVITY_ID` |
| [OUTCOME_ACTIVITY_RELTN](OUTCOME_ACTIVITY_RELTN.md) | `PARENT_OUTCOME_ACTIVITY_ID` |
| [OUTCOME_CRITERIA](OUTCOME_CRITERIA.md) | `OUTCOME_ACTIVITY_ID` |

