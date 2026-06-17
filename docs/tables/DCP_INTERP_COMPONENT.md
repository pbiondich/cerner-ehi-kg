# DCP_INTERP_COMPONENT

> Stores components used to interpret a result.

**Description:** DCP INTERP COMPONENT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPONENT_ASSAY_CD` | DOUBLE | NOT NULL |  | Task Assay Cd of the component. The component helps determine the value for the interp. |
| 2 | `COMPONENT_SEQUENCE` | DOUBLE | NOT NULL |  | Sequence number of the component. |
| 3 | `DCP_INTERP_COMPONENT_ID` | DOUBLE | NOT NULL |  | Unique Identifier |
| 4 | `DCP_INTERP_ID` | DOUBLE | NOT NULL | FK→ | Id of interp that this component is for. |
| 5 | `DESCRIPTION` | VARCHAR(200) |  |  | Description of component. |
| 6 | `FLAGS` | DOUBLE |  |  | Flags which identify properties of the component 1 - Numeric Component |
| 7 | `LOOK_AHEAD_MINUTES` | DOUBLE |  |  | The amount of time in minutes to look ahead from the documentation time of an interpretation for using a result as a contributor. |
| 8 | `LOOK_BACK_MINUTES` | DOUBLE |  |  | The amount of time in minutes to look back from the documentation time of an interpretation for using a result as a contributor. |
| 9 | `LOOK_TIME_DIRECTION_FLAG` | DOUBLE |  |  | Identifies to use look_back_minutes and look_ahead_minutes in an order. 0: Look back first and then look ahead; 1: Look ahead first and then look back. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DCP_INTERP_ID` | [DCP_INTERP](DCP_INTERP.md) | `DCP_INTERP_ID` |

