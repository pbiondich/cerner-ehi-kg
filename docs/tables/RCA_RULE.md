# RCA_RULE

> Represents a rule for the Revenue Cycle Solution

**Description:** Revenue Cycle Ambulatory - Rule  
**Table type:** REFERENCE  
**Primary key:** `RCA_RULE_ID`  
**Columns:** 17  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIONS_LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | The XML representation of the actions for the RCA_RULE row when the condition return is true. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `CATEGORY_MEANING_TXT` | VARCHAR(100) |  |  | The type of RCA_RULE that is used to categorize the RCA_RULE rows. |
| 4 | `CONDITION_LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | The XML representation of the condition for the RCA_RULE row. |
| 5 | `DESCRIPTION_TXT` | VARCHAR(255) |  |  | The description of the RCA_RULE row that is displayed to end users and provides more detail than the Display_txt value. |
| 6 | `DISPLAY_TXT` | VARCHAR(100) |  |  | The display or name value of the RCA_RULE row that is displayed to end users. |
| 7 | `ELSE_ACTIONS_LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | The XML representation of the actions for the RCA_RULE row when the condition returns false. |
| 8 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 9 | `MAJOR_SCHEMA_VERSION_NBR` | DOUBLE | NOT NULL |  | Defines the major version of an RCA rule. |
| 10 | `RCA_RULE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a rule for the Revenue Cycle Solution |
| 11 | `SCHEMA_VERSION_NBR` | DOUBLE | NOT NULL |  | The current version of the schema that the RCA_RULE row is build on top of. |
| 12 | `TYPE_MEANING_TXT` | VARCHAR(100) |  |  | The sub type of RCA_RULE that is used to categorize the RCA_RULE rows inn addition to the type_meaning column. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIONS_LONG_BLOB_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |
| `CONDITION_LONG_BLOB_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |
| `ELSE_ACTIONS_LONG_BLOB_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [RCA_CONVERSATION_RULE_R](RCA_CONVERSATION_RULE_R.md) | `RCA_RULE_ID` |
| [RCA_NOTIFICATION](RCA_NOTIFICATION.md) | `RCA_RULE_ID` |
| [RCA_RULE_RULE_RELTN](RCA_RULE_RULE_RELTN.md) | `CHILD_RCA_RULE_ID` |
| [RCA_RULE_RULE_RELTN](RCA_RULE_RULE_RELTN.md) | `PARENT_RCA_RULE_ID` |
| [RCA_RULE_SERVICE_RELTN](RCA_RULE_SERVICE_RELTN.md) | `RCA_RULE_ID` |

