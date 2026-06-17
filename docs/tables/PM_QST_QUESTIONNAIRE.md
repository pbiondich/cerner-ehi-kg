# PM_QST_QUESTIONNAIRE

> Person Mgmt: Defines flexible questionnaires.

**Description:** PM QST QUESTIONNAIRE  
**Table type:** REFERENCE  
**Primary key:** `QUESTIONNAIRE_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Name of the table that this questionnaire is associated with. |
| 2 | `QUESTIONNAIRE_COND` | VARCHAR(255) |  |  | (Future Use) |
| 3 | `QUESTIONNAIRE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the pm_qst_questionnaire table. It is an internal system assigned number. |
| 4 | `QUESTIONNAIRE_NAME` | VARCHAR(255) | NOT NULL |  | Name that identifies the questionnaire. |
| 5 | `QUESTIONNAIRE_TYPE_FLAG` | DOUBLE |  |  | Setting this to a 0 specifies a generic questionnaire. A value of 1 specifies a MSP questionnaire; 2 Cerner Practice Management (CPM) MSP Questionnaire. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PM_QST_QUESTIONNAIRE_ACT](PM_QST_QUESTIONNAIRE_ACT.md) | `QUESTIONNAIRE_ID` |

