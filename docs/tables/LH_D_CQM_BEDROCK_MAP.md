# LH_D_CQM_BEDROCK_MAP

> This table is used to store reference data based off of the Clinical Quality Measures Bedrock components

**Description:** LH_D_CQM_BEDROCK_MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | When the row is first activated |
| 2 | `CATEGORY_MEAN` | VARCHAR(100) |  |  | Unique string for a category |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | When the row becomes inactive |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. This field should be the same across all files and across all records within a file for a given extraction run. This time should be in UTC time. |
| 5 | `FILTER_MEAN` | VARCHAR(100) |  |  | Unique string for a filter |
| 6 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 7 | `LH_D_CQM_BEDROCK_MAP_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_D_CQM_BEDROCK_MAP table. |
| 8 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 9 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The Millennium value stored on the Bedrock table |
| 10 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 11 | `SOURCE_VOCAB_ITEM_IDENT` | VARCHAR(50) |  |  | The identifier that the Millennium value is mapped to |
| 12 | `SOURCE_VOCAB_MEAN` | VARCHAR(50) |  |  | The type of identifier as identified by CMS |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated |
| 15 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record |
| 16 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row |
| 17 | `VALUE_SET_NAME` | VARCHAR(255) |  |  | The CMS Value Set Name |
| 18 | `VOCAB_OID_TXT` | VARCHAR(100) |  |  | The CMS Value Set Identifier |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

