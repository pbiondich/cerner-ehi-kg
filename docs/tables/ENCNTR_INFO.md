# ENCNTR_INFO

> The encounter information table may contain a variety of information related to an encounter, not otherwise defined in the HNA database. It represents a code set driven method of extending the HNA database for Cerner and user defined data.

**Description:** Encounter Information  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_INFO_ID`  
**Columns:** 25  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHARTABLE_IND` | DOUBLE |  |  | Defines whether this encounter level comment can be shown on a chart. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 9 | `ENCNTR_INFO_ID` | DOUBLE | NOT NULL | PK | Primary Key for ENCNTR_INFO. Internal assigned number. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `INFO_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Auxilliary information which further specifies the type of encounter information contained in the row. A sub-category of the info_type_cd value. |
| 12 | `INFO_TYPE_CD` | DOUBLE | NOT NULL |  | The specific type of encounter information contained on the row. Examples may include comments and user-defined fields. |
| 13 | `INTERNAL_SEQ` | DOUBLE |  |  | Cerner-owned internal sequence which can be used to order given types of encounter information. |
| 14 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Foreign key to the LONG_TEXT table. Ties a long_text row (such as a comment) to this table. Encntr_info_id becomes the parent_entity_id on the long_text table, and "ENCNTR_INFO" becomes the parent_entity_name. |
| 15 | `PRIORITY_SEQ` | DOUBLE |  |  | Identifies a sequencing priority to be used when a duplicate relationship of the same type is created. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `VALUE_CD` | DOUBLE |  |  | Note: NOT tied specifically to codeset 1! Varies based on the type of encounter information being stored. For example, codified comments may be stored here, or the value for a codified user-defined field, or others. Values in this column will originate from various codesets depending on their intended use. |
| 22 | `VALUE_DT_TM` | DATETIME |  |  | The date and time value of the encounter information. If the value of the row necessitates storing a date/time, it is placed in this column. |
| 23 | `VALUE_NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | The nomenclature identifier value of the encounter information. If the value of the row necessitates storing a nomenclature identifier value, it is placed in this column. |
| 24 | `VALUE_NUMERIC` | DOUBLE |  |  | The numeric (non-codified) value of the encounter information. If the value of the row necessitates storing a numeric (non-codified) value, it is placed in this column. |
| 25 | `VALUE_NUMERIC_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the input from the front end tool for column VALUE_NUMBER is 0 or NULL. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `VALUE_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ENCNTR_INFO_HIST](ENCNTR_INFO_HIST.md) | `ENCNTR_INFO_ID` |

