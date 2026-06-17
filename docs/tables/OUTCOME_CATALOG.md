# OUTCOME_CATALOG

> Used to hold outcome definitions

**Description:** Outcome catalog table  
**Table type:** REFERENCE  
**Primary key:** `OUTCOME_CATALOG_ID`  
**Columns:** 30  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_DT_TM` | DATETIME | NOT NULL |  | Active date and timeColumn |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CONCEPT_CKI` | VARCHAR(255) |  |  | Unique CKI identifier |
| 6 | `DESCRIPTION` | VARCHAR(100) | NOT NULL |  | Description for a particular outcome |
| 7 | `DESCRIPTION_A_NLS` | VARCHAR(400) |  |  | DESCRIPTION_A_NLS column |
| 8 | `DESCRIPTION_KEY` | VARCHAR(100) | NOT NULL |  | Formatted outcome descriptionColumn |
| 9 | `DESCRIPTION_NLS` | VARCHAR(100) |  |  | Formatted outcome descriptionColumn |
| 10 | `EVENT_CD` | DOUBLE | NOT NULL | FK→ | Event code from v500_event_code which is used to identify relevant results |
| 11 | `EXPECTATION` | VARCHAR(200) | NOT NULL |  | Expected value for the outcome formatted from the outcome criteria built by the users |
| 12 | `EXPECTATION_A_NLS` | VARCHAR(400) |  |  | EXPECTATION_A_NLS column |
| 13 | `EXPECTATION_KEY` | VARCHAR(200) | NOT NULL |  | Formatted expected value for the outcome formatted from the outcome criteria built by the users |
| 14 | `EXPECTATION_NLS` | VARCHAR(200) |  |  | Formatted expected value for the outcome formatted from the outcome criteria built by the users |
| 15 | `HIDE_EXPECTATION_IND` | DOUBLE | NOT NULL |  | Used to suppress the display of outcome expectation string in the front end application. |
| 16 | `NOMEN_STRING_FLAG` | DOUBLE | NOT NULL |  | Identifies which nomenclature table field will be used to display the alpha response. 0 - Short String 1 - Mnemonic 2 - Source String |
| 17 | `OPERAND_MEAN` | CHAR(12) |  |  | Meaning that defines the operand when multiple alpha responses are used to define an outcome (AND or OR) |
| 18 | `OUTCOME_CATALOG_ID` | DOUBLE | NOT NULL | PK | Unique identifier for a particular outcome |
| 19 | `OUTCOME_CLASS_CD` | DOUBLE | NOT NULL |  | Outcome class codeColumn |
| 20 | `OUTCOME_TYPE_CD` | DOUBLE | NOT NULL |  | Outcome type code - outcome type identifier |
| 21 | `REFERENCE_TASK_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for a task that is used to chart values for the outcome. FK from ORDER_TASK table. |
| 22 | `REF_TEXT_RELTN_ID` | DOUBLE | NOT NULL |  | Unique identifier used to link outcome definition to the appropriate version of reference text defined for the outcome. |
| 23 | `RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | Format type of the result value which is used to evaluate the outcome |
| 24 | `SINGLE_SELECT_IND` | DOUBLE | NOT NULL |  | Used in conjunction with multi-criteria outcomes to indicate that only a single value can be selected when charting results against this outcome in Document In Plan view. |
| 25 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | DTA from discrete_task_assay table which is used to identify an event_cd and criteria values for the outcome definition |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EVENT_CD` | [V500_EVENT_CODE](V500_EVENT_CODE.md) | `EVENT_CD` |
| `REFERENCE_TASK_ID` | [ORDER_TASK](ORDER_TASK.md) | `REFERENCE_TASK_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [OUTCOME_ACTIVITY](OUTCOME_ACTIVITY.md) | `OUTCOME_CATALOG_ID` |
| [OUTCOME_CAT_CRITERIA](OUTCOME_CAT_CRITERIA.md) | `OUTCOME_CATALOG_ID` |
| [OUTCOME_CAT_LOC_RELTN](OUTCOME_CAT_LOC_RELTN.md) | `OUTCOME_CATALOG_ID` |

