# CDI_RULE_CRITERIA

> Defines the criteria for a rule used to The criteria for determining if the associated parent entity matches another entity's metadata.

**Description:** CDI Rule Criteria  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_RULE_CRITERIA_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CDI_RULE_CRITERIA table. |
| 2 | `CDI_RULE_ID` | DOUBLE | NOT NULL | FK→ | The rule that this criteria pertains to. |
| 3 | `COMPARISON_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of comparison to perform. 0 - equals, 1 - less than, 2 - greater than, 3 - not equal, 4 - less than or equal, 5 - greater than or equal |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This field contains the identifier for the parent table row. |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | This field contains the name of table that this cdi_rule row is associated to. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `VALUE_CD` | DOUBLE | NOT NULL |  | the code value to compare against. code set will vary. |
| 12 | `VALUE_DT_TM` | DATETIME |  |  | Date value to compare against. |
| 13 | `VALUE_ENTITY_ID` | DOUBLE |  |  | This field contains the identifier for the parent table row. |
| 14 | `VALUE_ENTITY_NAME` | VARCHAR(30) |  |  | This field contains the name of table that this cdi_rule row is associated to. |
| 15 | `VALUE_NBR` | DOUBLE | NOT NULL |  | numeric value to compare against. |
| 16 | `VALUE_TXT` | VARCHAR(100) | NOT NULL |  | String value to compare against. |
| 17 | `VARIABLE_CD` | DOUBLE | NOT NULL |  | Identifies the variable (encounter data, etc.) that this criteria is evaluated against. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_RULE_ID` | [CDI_RULE](CDI_RULE.md) | `CDI_RULE_ID` |

