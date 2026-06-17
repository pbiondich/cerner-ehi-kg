# RAD_TECH_FLD_FMT_R

> The rad_tech_fld_fmt_r table holds a relation between a technical comment format and a list fields for that format.

**Description:** Radiology Tech comment field format relations.  
**Table type:** REFERENCE  
**Primary key:** `FIELD_FORMAT_RELTN_ID`  
**Columns:** 22  
**Referenced by:** 1 columns

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
| 10 | `FIELD_FORMAT_RELTN_ID` | DOUBLE | NOT NULL | PK | The field_format_reltn_Id uniquely identifies a row in the Rad_Tech_Fld_Fmt_r table. It serves no other purpose other than to uniquely identify the row |
| 11 | `FIELD_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a field. FK from the Rad_tech_field table. |
| 12 | `FORMAT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a format. FK from the rad_tech_format table. |
| 13 | `MAX_NBR` | DOUBLE |  |  | The max_nbr field holds a maximum numerical value. It can only be set for a field that is a number type. |
| 14 | `MIN_NBR` | DOUBLE |  |  | The min_nbr field holds a minimum numerical value. It can only be set for a field that is a number type. |
| 15 | `PARENT_FIELD_ID` | DOUBLE | NOT NULL | FK→ | The Parent_Field_Id is a foreign key to the Rad_Tech_Field table. It is used to identify a parent field for the row. |
| 16 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | The Required_ind defines if this field is required to be filled out before exam completion |
| 17 | `SEQUENCE` | DOUBLE | NOT NULL |  | The Sequence identifies an order of fields within a specific format. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FIELD_ID` | [RAD_TECH_FIELD](RAD_TECH_FIELD.md) | `FIELD_ID` |
| `FORMAT_ID` | [RAD_TECH_FORMAT](RAD_TECH_FORMAT.md) | `FORMAT_ID` |
| `PARENT_FIELD_ID` | [RAD_TECH_FIELD](RAD_TECH_FIELD.md) | `FIELD_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RAD_TECH_FMT_ERPRC_OVRD](RAD_TECH_FMT_ERPRC_OVRD.md) | `FIELD_FORMAT_RELTN_ID` |

