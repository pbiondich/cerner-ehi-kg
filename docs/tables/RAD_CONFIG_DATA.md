# RAD_CONFIG_DATA

> This table holds RadNet system configuration data. This table is meant to replace tables that are specific to certain functionality.

**Description:** Configuration data for system controls.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BREAST_DENSITY_TEXT` | VARCHAR(2000) |  |  | Contains the Breast Density Statement for the given Parent Entity Id. |
| 2 | `CONTROL_CHAR` | VARCHAR(255) |  |  | Holds the string value of the control named by control_name. |
| 3 | `CONTROL_DT_TM` | DATETIME |  |  | Holds the date/time value of the control named by control_name. |
| 4 | `CONTROL_NAME` | VARCHAR(255) |  |  | The name of the specific database setting. |
| 5 | `CONTROL_NUMBER` | DOUBLE | NOT NULL |  | Holds the numeric value of the control named by control_name. |
| 6 | `DOMAIN_CD` | DOUBLE | NOT NULL |  | Describes the group of settings that this row pertains to. |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The primary id of the table that this row is a child of. |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(255) |  |  | The name of the table that the row on this table is a child of. |
| 9 | `RAD_CONFIG_DATA_ID` | DOUBLE | NOT NULL |  | The rad_config_data_id uniquely identifies a row in the Rad_config_data table. It serves no other purpose other than to uniquely identify the row. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

