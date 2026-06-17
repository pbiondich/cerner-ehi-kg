# RC_CONFIG_SUBSYSTEM

> This table will define a configuration subsystem or document type. Example: "genesis:infusion-documentation-1.0"

**Description:** Revenue Cycle Configuration Subsystem  
**Table type:** REFERENCE  
**Primary key:** `RC_CONFIG_SUBSYSTEM_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RC_CONFIG_SUBSYSTEM_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RC_CONFIG_SUBSYSTEM |
| 2 | `UNIFORM_RESOURCE_NAME` | VARCHAR(200) | NOT NULL |  | The name of this subsystem. Can be thought of as the "type" of a configuration document. |
| 3 | `UNIFORM_RESOURCE_NAME_KEY` | VARCHAR(200) | NOT NULL |  | The Key value of the UNIFORM_RESOURCE_NAME column. Contains the value in the UNIFORM_RESOURCE_NAME column in all caps with special characters removed. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RC_CONFIG_DOCUMENT](RC_CONFIG_DOCUMENT.md) | `RC_CONFIG_SUBSYSTEM_ID` |

