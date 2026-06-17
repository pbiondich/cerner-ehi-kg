# DCP_CONFIG_COMP_RELTN

> This table contains data to form a relation using Config_component table's config_components_id column with configuration_setting table's configuration_setting_id column

**Description:** Component configuration setting relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DCP_CONFIG_COMP_ID` | DOUBLE | NOT NULL | FK→ | identifier for a Component in config_components table |
| 2 | `DCP_CONFIG_COMP_RELTN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `DCP_CONFIG_SETTING_ID` | DOUBLE | NOT NULL | FK→ | identifier for a Component in configuration_setting table |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DCP_CONFIG_COMP_ID` | [DCP_CONFIG_COMP](DCP_CONFIG_COMP.md) | `DCP_CONFIG_COMP_ID` |
| `DCP_CONFIG_SETTING_ID` | [DCP_CONFIG_SETTING](DCP_CONFIG_SETTING.md) | `DCP_CONFIG_SETTING_ID` |

