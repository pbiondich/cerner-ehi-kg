# V500_EVENT_SET_CODE

> Contains extra fields for event sets not stored in the code_value table

**Description:** V500 event set code table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCUMULATION_IND` | DOUBLE |  |  | Display the accumulation of the numeric data element as it occurs in the flowsheet. i.e. 25/25, 5/30, 15/45 ... |
| 2 | `CATEGORY_FLAG` | DOUBLE |  |  | User defined level indicating the level of grouping for the event set 7 '1' Flowsheet level 7 '2' Category level 7 '3' Section level 7 '4' Group level |
| 3 | `CODE_STATUS_CD` | DOUBLE | NOT NULL |  | data status code of this row |
| 4 | `COMBINE_FORMAT` | VARCHAR(200) |  |  | Defines the format for composite fields. i.e. (bp dia / bp sys) |
| 5 | `DISPLAY_ASSOCIATION_IND` | DOUBLE | NOT NULL |  | The grouping of Event codes can be accomplished by setting the display_association_ind for the primitive + 1 level to allow for grouping all of the primitives below this group into a single flowsheet cell. Front end applications will handle the grouping as required. |
| 6 | `EVENT_SET_CD` | DOUBLE | NOT NULL |  | unique primary key for this table |
| 7 | `EVENT_SET_CD_DEFINITION` | VARCHAR(100) |  |  | Definition of event set |
| 8 | `EVENT_SET_CD_DESCR` | VARCHAR(60) |  |  | Description of the event set |
| 9 | `EVENT_SET_CD_DISP` | VARCHAR(40) |  |  | Display of event set |
| 10 | `EVENT_SET_CD_DISP_KEY` | VARCHAR(40) |  |  | Key of event set display |
| 11 | `EVENT_SET_COLOR_NAME` | VARCHAR(16) |  |  | Not currently used |
| 12 | `EVENT_SET_ICON_NAME` | VARCHAR(16) |  |  | Not currently used |
| 13 | `EVENT_SET_NAME` | VARCHAR(40) | NOT NULL |  | Name of the event set |
| 14 | `EVENT_SET_NAME_KEY` | VARCHAR(40) |  |  | Name key of the event set |
| 15 | `EVENT_SET_NAME_UPPER_VC` | VARCHAR(40) |  |  | Uppercase version of EVENT_SET_NAME |
| 16 | `EVENT_SET_STATUS_CD` | DOUBLE | NOT NULL |  | Authentication status of event set |
| 17 | `GROUPING_RULE_FLAG` | DOUBLE |  |  | Defines rules on how to display data for an event set when there are more than one result in the cell 7 '1' First result in the valid cell range 7 '2' Last result in the valid cell range 7 '3' Sum of all results 7 '4' Average of all results 7 '5' Median 7 '6' Count |
| 18 | `LEAF_EVENT_CD_COUNT` | DOUBLE |  |  | Not currently used |
| 19 | `OPERATION_DISPLAY_FLAG` | DOUBLE |  |  | Determines how to display the calculated result 7 '1' Before the first event set 7 '2' After the last event set 7 '3' Only display the calculated results but not the individual event sets |
| 20 | `OPERATION_FORMULA` | VARCHAR(200) |  |  | A string of characters that describes the formula for a calculation i.e. (bp dia + bp sys)/2, Sum(IV), etc. |
| 21 | `PRIMITIVE_EVENT_SET_COUNT` | DOUBLE |  |  | Not currently used |
| 22 | `SHOW_IF_NO_DATA_IND` | DOUBLE |  |  | Determines if the data element ought to be displayed if it does not contain any data within the flowsheet valid time range |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

