# MIC_SCRIPT

> This reference table contains a single record for every Microbiology 'organism scripted work-up' (Script).

**Description:** Microbiology Scripted Workup  
**Table type:** REFERENCE  
**Primary key:** `SCRIPT_ID`  
**Columns:** 8  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXCLUDE_TECH_IND` | DOUBLE |  |  | This indicator field is used to determine whether Microbiology techs defined on the MIC_SCRIPT_TECH table can run the script or not. A value of 1 indicates that techs on the MIC_SCRIPT_TECH table can NOT run the script. |
| 2 | `SCRIPT_ID` | DOUBLE | NOT NULL | PK | This field contains the internal identification code that uniquely identifies the 'organism scripted work-up' and its associated parameters. This value is used to join to the MIC_SCRIPT_* tables. |
| 3 | `SCRIPT_NAME` | VARCHAR(40) | NOT NULL |  | This field contains a unique name for a script. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [MIC_SCRIPT_CRITERIA](MIC_SCRIPT_CRITERIA.md) | `SCRIPT_ID` |
| [MIC_SCRIPT_NODE](MIC_SCRIPT_NODE.md) | `SCRIPT_ID` |
| [MIC_SCRIPT_TECH](MIC_SCRIPT_TECH.md) | `SCRIPT_ID` |

