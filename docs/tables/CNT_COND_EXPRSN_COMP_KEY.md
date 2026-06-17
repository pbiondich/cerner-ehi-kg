# CNT_COND_EXPRSN_COMP_KEY

> Contains details about working view conditional expression components which are used by Bedroc tool. Imported using content manager tool.

**Description:** CNT_COND_EXPRSN_COMP_KEY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AR_UID` | VARCHAR(100) | NOT NULL |  | UID of Alpha response. |
| 3 | `CNT_COND_EXPRSN_COMP_KEY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `CNT_COND_EXPRSN_COMP_KEY_UID` | VARCHAR(100) |  |  | UID(Unique Identification) number which is used in versioning of conditional expression component in conjunction with version_dt_tm column. |
| 5 | `COND_COMP_NAME` | VARCHAR(30) |  |  | Unique description for the component for the expression |
| 6 | `COND_EXPRSN_COMP_ID` | DOUBLE | NOT NULL |  | Unique value for the expression component |
| 7 | `COND_EXPRSN_ID` | DOUBLE | NOT NULL |  | references CNT_COND_EXPRESSION_KEY.COND_EXPRESSION_ID |
| 8 | `DCP_COND_EXP_COMP_ID_REF_ID` | DOUBLE | NOT NULL | FK→ | refers to original COND_EXPRESSION_COMP table which is used by bedrock tool |
| 9 | `OPERATOR_CD` | DOUBLE | NOT NULL |  | stores comparison operator between the trigger DTA and logical operator |
| 10 | `OPERATOR_CD_UID` | VARCHAR(100) |  |  | UID of the operator code which is used for versioning |
| 11 | `PREV_COND_EXPRSN_COMP_ID` | DOUBLE | NOT NULL |  | Unique identifier of the original version. |
| 12 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Required indicator for the conditionality |
| 13 | `RESULT_VALUE` | DOUBLE | NOT NULL |  | result value that evaluates the component |
| 14 | `TRIGGER_ASSAY_CD` | DOUBLE | NOT NULL |  | The DTA which enable or disable the other DTA's. |
| 15 | `TRIGGER_ASSAY_CD_UID` | VARCHAR(100) |  |  | UID of the DTA which is used for versioning |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `VERSION_DT_TM` | DATETIME |  |  | Date and time when this record was updated. Used in versioning of the conditional expression component in conjunction with UID column |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DCP_COND_EXP_COMP_ID_REF_ID` | [COND_EXPRESSION_COMP](COND_EXPRESSION_COMP.md) | `COND_EXPRESSION_COMP_ID` |

