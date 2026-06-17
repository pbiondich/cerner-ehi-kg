# DCP_CONFIG_SETTING

> This table contains details about a single configuration setting

**Description:** Configuration Setting  
**Table type:** REFERENCE  
**Primary key:** `DCP_CONFIG_SETTING_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONFIG_DESC` | VARCHAR(2000) |  |  | Long description about a configuration that provides user with extra information about a configuration |
| 2 | `CONFIG_DISPLAY` | VARCHAR(140) | NOT NULL |  | Name of a configuration that is displayed to user |
| 3 | `CONFIG_DOMAIN` | VARCHAR(32) | NOT NULL |  | Specifies what type of domain setting it is (preference, privileges,application groups etc.) |
| 4 | `CONFIG_NAME` | VARCHAR(256) | NOT NULL |  | Unique name assigned to a configuration setting(e.g.: pvc_name, priv_name) |
| 5 | `CONFIG_TYPE` | VARCHAR(32) | NOT NULL |  | Defines what type of domain setting a configuration is (view,detail, viewcomp, message center etc.) |
| 6 | `DCP_CONFIG_SETTING_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 7 | `REFURL_TXT` | VARCHAR(256) |  |  | Link to the help page that provides extra information about a configuration |
| 8 | `STANDARD_IND` | DOUBLE | NOT NULL |  | Indicator that tells whether a configuration has a standard or not (1-standard,0 : non-standard) |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DCP_CONFIG_COMP_RELTN](DCP_CONFIG_COMP_RELTN.md) | `DCP_CONFIG_SETTING_ID` |

