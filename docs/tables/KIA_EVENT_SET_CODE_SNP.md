# KIA_EVENT_SET_CODE_SNP

> Event Set snapshot. - This table is a copy of the V500_Event_set_code table

**Description:** Event Set snapshot  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCUMULATION_IND` | DOUBLE |  |  | display the accumulation of the numeric data element as it occurs in the flowsheet. i.e. 25/25, 5/30, 15/45 ... |
| 2 | `CATEGORY_FLAG` | DOUBLE |  |  | user defined level indicating the level of grouping for the event set 7 '1' flowsheet level 7 '2' category level 7 '3' section level 7 '4' group level |
| 3 | `CODE_STATUS_CD` | DOUBLE | NOT NULL |  | data status code of this row.Column |
| 4 | `COMBINE_FORMAT` | VARCHAR(200) |  |  | defines the format for composite fields.i.e. (bp dia / bp sys) |
| 5 | `DISPLAY_ASSOCIATION_IND` | DOUBLE | NOT NULL |  | the grouping of event codes can be accomplished by setting the display_association_ind for the primitive + 1 level to allow for grouping all of the primitives below this group into a single flowsheet cell. front end applications will handle the grouping as required. |
| 6 | `EVENT_SET_CD` | DOUBLE | NOT NULL |  | unique primary key for this table.Column |
| 7 | `EVENT_SET_CD_DEFINITION` | VARCHAR(100) |  |  | definition of the event set.Column |
| 8 | `EVENT_SET_CD_DESCR` | VARCHAR(60) |  |  | description of the event set.Column |
| 9 | `EVENT_SET_CD_DISP` | VARCHAR(40) |  |  | display of event setColumn |
| 10 | `EVENT_SET_CD_DISP_KEY` | VARCHAR(40) |  |  | key of the event set displayColumn |
| 11 | `EVENT_SET_COLOR_NAME` | VARCHAR(16) |  |  | not currently usedColumn |
| 12 | `EVENT_SET_ICON_NAME` | VARCHAR(16) |  |  | not currently usedColumn |
| 13 | `EVENT_SET_NAME` | VARCHAR(40) | NOT NULL |  | name of the event setColumn |
| 14 | `EVENT_SET_NAME_KEY` | VARCHAR(40) |  |  | name key of the event setColumn |
| 15 | `EVENT_SET_STATUS_CD` | DOUBLE | NOT NULL |  | authentication status of the event setColumn |
| 16 | `GROUPING_RULE_FLAG` | DOUBLE |  |  | defines rules on how to display data for an event set when there are more than one result in the cell 7 '1' first result in the valid cell range 7 '2' last result in the valid cell range 7 '3' sum of all results |
| 17 | `LEAF_EVENT_CD_COUNT` | DOUBLE |  |  | not currently usedColumn |
| 18 | `OPERATION_DISPLAY_FLAG` | DOUBLE |  |  | determines how to display the calculated result 7 '1' before the first event set 7 '2' after the last event set 7 '3' only display the calculated results but not the individual event sets |
| 19 | `OPERATION_FORMULA` | VARCHAR(200) |  |  | a string of characters that describes the formula for a calculation i.e. (bp dia + bp sys)/2, sum(iv), etc. |
| 20 | `PRIMITIVE_EVENT_SET_COUNT` | DOUBLE |  |  | not currently usedColumn |
| 21 | `SHOW_IF_NO_DATA_IND` | DOUBLE |  |  | determines if the data element ought to be displayed if it does not contain any data within the flowsheet valid time range |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

