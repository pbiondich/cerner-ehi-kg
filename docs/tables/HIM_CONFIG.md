# HIM_CONFIG

> Stores configuration information for Health Information Management solutions.

**Description:** HIM Configuration  
**Table type:** REFERENCE  
**Primary key:** `HIM_CONFIG_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GROUP_NAME` | VARCHAR(50) | NOT NULL |  | Name used to group a collection of configuration items. |
| 2 | `HIM_CONFIG_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the HIM_CONFIG table. |
| 3 | `JSON_VALUE_TXT` | LONGBLOB |  |  | Value used for configuration as a JSON. |
| 4 | `JSON_VRSN_TXT` | VARCHAR(20) |  |  | A version of the JSON schema must held in a separate Oracle column externalized from the JSON itself. The JSON version will change as the schema of the JSON changes. |
| 5 | `KEY_NAME` | VARCHAR(50) | NOT NULL |  | Key used to identify the configuration item. |
| 6 | `LAST_MODIFIED_DT_TM` | DATETIME | NOT NULL |  | The date that the configuration was last modified. |
| 7 | `LAST_MODIFIED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Foreign key, Unique generated number that identifies a single row on the PRSNL table. Last person that modified the row. |
| 8 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 9 | `MULTI_CONFIG_NBR` | DOUBLE | NOT NULL |  | Use to prevent duplicates when configuration has no entry in the HIM_CONFIG_INDEX table. |
| 10 | `SUBGROUP_NAME` | VARCHAR(50) | NOT NULL |  | Name used to identify a sub group of configuration items. |
| 11 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `VALUE_TXT` | VARCHAR(250) |  |  | Value used for configuration as a string. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LAST_MODIFIED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [HIM_CONFIG_INDEX](HIM_CONFIG_INDEX.md) | `HIM_CONFIG_ID` |

