# CHART_LISTVIEW_FORMAT

> Stores configuration data related to the list view chart section (CHART_GROUP_ID should be the MUI)

**Description:** Chart List View Format  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_SEQ` | DOUBLE | NOT NULL |  | Sequence of the "Accession Number" column, if appearing on the chart |
| 2 | `ACCESSION_TXT` | VARCHAR(32) |  |  | Label appearing on the chart when the "Accession Number" column appears |
| 3 | `CHART_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Refers to the group_id on chart_group |
| 4 | `CHART_LISTVIEW_FORMAT_ID` | DOUBLE | NOT NULL |  | System-assigned ID column. |
| 5 | `COLLECTED_DT_TM_SEQ` | DOUBLE | NOT NULL |  | Sequence of the "Collected dt/tm" column, if appearing on the chart |
| 6 | `COLLECTED_TXT` | VARCHAR(32) |  |  | Label appearing on the chart when the "Collected dt/tm" column appears |
| 7 | `DATE_MASK` | VARCHAR(32) |  |  | Formatting attribute for dates displayed on printed chart. Ex: "mm/dd/yyyy" |
| 8 | `GROUP_RESULT_SEQ` | DOUBLE | NOT NULL |  | Sequence of the "Result" column, if appearing on the chart. |
| 9 | `PERF_VER_PRSNL_SEQ` | DOUBLE | NOT NULL |  | Sequence of the "Performed/Verified By:" column, if appearing on the chart |
| 10 | `PERF_VER_PRSNL_TXT` | VARCHAR(32) |  |  | Label appearing on the chart when the "Performed/Verified By" column appears |
| 11 | `PROCEDURE_SEQ` | DOUBLE | NOT NULL |  | Sequence of the "Procedure" column, if appearing on the chart |
| 12 | `PROCEDURE_TXT` | VARCHAR(32) |  |  | Label appearing on the chart when the "Procedure" column appears |
| 13 | `RECEIVED_DT_TM_SEQ` | DOUBLE | NOT NULL |  | Sequence of the "Received dt/tm" column, if appearing on the chart |
| 14 | `RECEIVED_TXT` | VARCHAR(32) |  |  | Label appearing on the chart when the "Received dt/tm" column appears |
| 15 | `REFRANGE_SEQ` | DOUBLE | NOT NULL |  | Sequence of the "Reference Range" column, if appearing on the chart |
| 16 | `REFRANGE_TXT` | VARCHAR(32) |  |  | Label appearing on the chart when the "Reference Range" column appears |
| 17 | `REF_RNG_FORM_FLAG` | DOUBLE | NOT NULL |  | Stores a value indicating which of the two options for displaying the reference range has been selected. |
| 18 | `RESULT_SEQ` | DOUBLE | NOT NULL |  | Sequence of the "Result" column, if appearing on the chart. |
| 19 | `RESULT_TXT` | VARCHAR(32) |  |  | Label appearing on the chart when the "Result" column appears |
| 20 | `SPECTYPE_SEQ` | DOUBLE | NOT NULL |  | Sequence of the "Specimen Type" column, if appearing on the chart |
| 21 | `SPECTYPE_TXT` | VARCHAR(32) |  |  | Label appearing on the chart when the "Specimen Type" column appears |
| 22 | `TIME_MASK` | VARCHAR(32) |  |  | Formatting attribute for times displayed on printed chart. Ex: "hh:mm:ss" |
| 23 | `UNITS_SEQ` | DOUBLE | NOT NULL |  | Sequence of the "Units" column, if appearing on the chart |
| 24 | `UNITS_TXT` | VARCHAR(32) |  |  | Label appearing on the chart when the "Units" column appears |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 30 | `VERIFIED_DT_TM_SEQ` | DOUBLE | NOT NULL |  | Sequence of the "Verified dt/tm" column, if appearing on the chart |
| 31 | `VERIFIED_TXT` | VARCHAR(32) |  |  | Label appearing on the chart when the "Verified dt/tm" column appears |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_GROUP_ID` | [CHART_GROUP](CHART_GROUP.md) | `CHART_GROUP_ID` |

