# MIC_BPA_WORKLIST

> Stores the "parent-level" criteria for Microbiology BPA Worklists.

**Description:** Microbiology Breakpoint Worklist  
**Table type:** ACTIVITY  
**Primary key:** `WORKLIST_ID`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_TASK_DT_TM` | DATETIME |  |  | User-defined date/time which will be used to autogenerate the worklist details. |
| 2 | `DESCRIPTION` | VARCHAR(60) |  |  | Description of the worklist |
| 3 | `DISPLAY` | VARCHAR(40) | NOT NULL |  | Display value of the worklist |
| 4 | `FINALIZED_IND` | DOUBLE |  |  | Indicates whether of not the worklist has been finalized |
| 5 | `GROUP_BIOCHEMICAL_CD` | DOUBLE | NOT NULL |  | The internal identification code for the group biochemical that will be used in the worklist. (CS 1002) |
| 6 | `PLATE_CD` | DOUBLE | NOT NULL |  | The internal identification code for the plate definition. (CS 28081) |
| 7 | `QC_PANEL_CD` | DOUBLE | NOT NULL |  | The internal identification code for the QC panel that will be used in the worklist. (CS 28080) |
| 8 | `SUSCEPTIBILITY_METHOD_CD` | DOUBLE | NOT NULL |  | The internal identification code for the susceptibility method that will be used in the worklist. (CS 65) |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `WORKLIST_DT_TM` | DATETIME | NOT NULL |  | User-defined date associated with the worklist |
| 15 | `WORKLIST_ID` | DOUBLE | NOT NULL | PK | Internal identification code assigned to each breakpoint worklist. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MIC_BPA_WORKLIST_DETAIL](MIC_BPA_WORKLIST_DETAIL.md) | `WORKLIST_ID` |
| [MIC_BPA_WORKLIST_PANEL](MIC_BPA_WORKLIST_PANEL.md) | `WORKLIST_ID` |

