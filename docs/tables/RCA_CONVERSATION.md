# RCA_CONVERSATION

> Stores the details about conversation for the Revenue Cycle solution.

**Description:** Revenue Cycle Ambulatory - Conversation  
**Table type:** REFERENCE  
**Primary key:** `RCA_CONVERSATION_ID`  
**Columns:** 16  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CONVERSATION_TYPE_CD` | DOUBLE | NOT NULL |  | The type of Revenue Cycle conversation. |
| 3 | `CONVERSATION_UUID` | VARCHAR(100) | NOT NULL |  | Will uniquely identify the conversation universally. |
| 4 | `DESCRIPTION_TXT` | VARCHAR(255) |  |  | The description of the Revenue Cycle conversation. |
| 5 | `DISPLAY_TXT` | VARCHAR(100) |  |  | The display of the Revenue Cycle conversation. |
| 6 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 7 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the contents of the Revenue Cycle conversation. |
| 8 | `MAJOR_VERSION_NBR` | DOUBLE | NOT NULL |  | Defines the major version of a conversation. |
| 9 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | The priority sequence of the Revenue Cycle conversation compared to the other conversations of the same type. |
| 10 | `RCA_CONVERSATION_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies details about a conversation for the Revenue Cycle solution. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `VERSION_NBR` | DOUBLE | NOT NULL |  | The version number of the Revenue Cycle conversation. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `LONG_BLOB_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [RCA_CONVERSATION_RULE_R](RCA_CONVERSATION_RULE_R.md) | `RCA_CONVERSATION_ID` |
| [RCA_CONV_GROUP_CONV_R](RCA_CONV_GROUP_CONV_R.md) | `RCA_CONVERSATION_ID` |
| [RCA_REG_ACTION_CONV_RELTN](RCA_REG_ACTION_CONV_RELTN.md) | `RCA_CONVERSATION_ID` |

