# PW_VARIANCE_RELTN

> Table used to relate variance results to pathways and pathway components

**Description:** pw_variance_reltn  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_CD` | DOUBLE | NOT NULL |  | Codified action field to describe what action was taken to address the variance column. Values in this field may be from code set 30186 or 24931. |
| 2 | `ACTION_TEXT_ID` | DOUBLE | NOT NULL |  | Text_id of the free textaction description.Column |
| 3 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `CHART_DT_TM` | DATETIME |  |  | Date & time the variance was charted |
| 5 | `CHART_PRSNL_ID` | DOUBLE | NOT NULL |  | Unique identifier of the person who charted the variance |
| 6 | `CHART_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column |
| 7 | `EVENT_ID` | DOUBLE | NOT NULL |  | Event_id of the results that document the variance |
| 8 | `NOTE_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Text ID of the free textNote. Foreign key from LONG_TEXT table (LONG_TEXT_ID). |
| 9 | `OUTCOME_COMP_ID` | DOUBLE | NOT NULL | FK→ | Id of the pathway outcome component that this variance relates to. This will only be filled out for result variances that were charted as a result of the outcome. |
| 10 | `OUTCOME_OPERATOR_CD` | DOUBLE | NOT NULL |  | Codified outcome operator.Column |
| 11 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Id of the item the variance is related to (pathway, act_pw_comp, clinical_event). |
| 12 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Name of the parent entity the variance is related to. |
| 13 | `PATHWAY_ID` | DOUBLE | NOT NULL | FK→ | Id of the pathway the variance is related to. This field will always be filled out if the variance is related to a pathway, act_pw_comp, or outcome result. |
| 14 | `PW_VARIANCE_RELTN_ID` | DOUBLE | NOT NULL |  | Id of the variance relationship entry. |
| 15 | `REASON_CD` | DOUBLE | NOT NULL |  | Codified reason why the variance occurred. Values in this code column may be from code set 24930 or 30185. |
| 16 | `REASON_TEXT_ID` | DOUBLE | NOT NULL |  | Text_id of the free text reason.Column |
| 17 | `RESULT_UNITS_CD` | DOUBLE | NOT NULL |  | Result units of the result_value that are used to define the outcome.Column |
| 18 | `RESULT_VALUE` | DOUBLE |  |  | Result value used to define the outcome.Column |
| 19 | `UNCHART_DT_TM` | DATETIME |  |  | Date & time the variance was uncharted |
| 20 | `UNCHART_PRSNL_ID` | DOUBLE | NOT NULL |  | Unique identifier of the person who uncharted the variance |
| 21 | `UNCHART_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 27 | `VARIANCE_DT_TM` | DATETIME |  |  | Date and time the variance was created.Column |
| 28 | `VARIANCE_TYPE_CD` | DOUBLE | NOT NULL |  | Codified variance type.Column |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOTE_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `OUTCOME_COMP_ID` | [ACT_PW_COMP](ACT_PW_COMP.md) | `ACT_PW_COMP_ID` |
| `PATHWAY_ID` | [PATHWAY](PATHWAY.md) | `PATHWAY_ID` |

