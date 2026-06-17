# FIELD_CATALOG

> Field_Catalog

**Description:** Stores all field information pertaining to the Bill Template.  
**Table type:** REFERENCE  
**Primary key:** `FIELD_CATALOG_ID`  
**Columns:** 24  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BILL_TYPE_CD` | DOUBLE | NOT NULL |  | Codeset holding information about the different bill types |
| 7 | `CONTROL_NBR` | DOUBLE |  |  | Unique number used for internal processing |
| 8 | `ELEMENT_NAME` | VARCHAR(40) |  |  | Name of the corresponding element in the bill structure |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `FIELD_CATALOG_ID` | DOUBLE | NOT NULL | PK | Unique Id |
| 11 | `FIELD_DESC` | VARCHAR(250) |  |  | Defines what the field is used for |
| 12 | `FIELD_LOC_STRING` | VARCHAR(20) |  |  | Stores the field locator on the form (1500,1450) |
| 13 | `FIELD_NAME` | VARCHAR(250) |  |  | The name of the field |
| 14 | `FIELD_NAME_KEY` | VARCHAR(250) |  |  | The name of the field in Upper Case. This is used to search on. |
| 15 | `FIELD_TYPE_FLAG` | DOUBLE |  |  | Stores the default field type for that field |
| 16 | `LIST_INDEX` | DOUBLE | NOT NULL |  | Index to the corresponding list in the bill structrue |
| 17 | `LIST_NAME` | VARCHAR(40) |  |  | Name of the corresponding list in the bill structure |
| 18 | `MAX_FIELD_LENGTH` | DOUBLE |  |  | The maximumlength the field is able to handle |
| 19 | `MIN_FIELD_LENGTH` | DOUBLE |  |  | The minimumlength the field requires |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ATTRIB_FIELD_RELTN](ATTRIB_FIELD_RELTN.md) | `FIELD_CATALOG_ID` |
| [BR_FIELD_ERRORS](BR_FIELD_ERRORS.md) | `FIELD_CATALOG_ID` |
| [CLAIM_FLD_POSITION](CLAIM_FLD_POSITION.md) | `FIELD_CATALOG_ID` |

