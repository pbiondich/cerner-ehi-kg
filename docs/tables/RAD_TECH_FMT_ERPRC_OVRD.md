# RAD_TECH_FMT_ERPRC_OVRD

> The Rad_Tech_Fmt_ErProc_Ovrd table holds attributes about fields in a format ,for a given service resource and procedure, that are different than those specified just the format level.

**Description:** Radiology tech comment format attributes override  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHARTABLE_IND` | DOUBLE | NOT NULL |  | The Chartable_ind defines if this field is to be charted for this format. |
| 6 | `DEFAULT_CHOICE_IND` | DOUBLE |  |  | The Chartable_ind defines if this field is to be charted for this format. |
| 7 | `DEFAULT_DT_TM` | DATETIME |  |  | The Default_Date field holds date default data. |
| 8 | `DEFAULT_NBR` | DOUBLE |  |  | The Default_Nbr field holds numeric default data. |
| 9 | `DEFAULT_TEXT` | VARCHAR(255) |  |  | The Default_Text field holds textual default data. |
| 10 | `FIELD_FORMAT_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Field Format Relation identifier. |
| 11 | `FORMAT_ERPRC_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The Format_Erproc_reltn_Id is a foreign key to the Rad_Tech_Fmt_ErProc_r table. It is used to define a format that has had field attribute changes for a given procedure and an exam room. |
| 12 | `FORMAT_OVRD_ID` | DOUBLE | NOT NULL |  | The format_Ovrd_Id uniquely identifies a row in the Rad_Tech_Fmt_ErProc_Ovrd table. It serves no other purpose other than to uniquely identify the row |
| 13 | `MAX_NBR` | DOUBLE |  |  | The max_nbr field holds a maximum numerical value. It can only be set for a field that is a number type. |
| 14 | `MIN_NBR` | DOUBLE |  |  | The min_nbr field holds a maximum numerical value. It can only be set for a field that is a number type.. |
| 15 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | The Required_ind defines if this field is required to be filled out before exam completion |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FIELD_FORMAT_RELTN_ID` | [RAD_TECH_FLD_FMT_R](RAD_TECH_FLD_FMT_R.md) | `FIELD_FORMAT_RELTN_ID` |
| `FORMAT_ERPRC_RELTN_ID` | [RAD_TECH_FMT_ERPRC_R](RAD_TECH_FMT_ERPRC_R.md) | `FORMAT_ERPRC_RELTN_ID` |

