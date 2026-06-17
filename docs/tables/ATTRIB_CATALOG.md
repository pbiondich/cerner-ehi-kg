# ATTRIB_CATALOG

> Attrbute Catalog

**Description:** Stores information related to the attributes that will be used to create bills  
**Table type:** REFERENCE  
**Primary key:** `ATTRIB_CATALOG_ID`  
**Columns:** 23  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ATTRIB_CATALOG_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 6 | `ATTRIB_DESC` | VARCHAR(250) |  |  | Description of the attribute. |
| 7 | `ATTRIB_NAME` | VARCHAR(250) |  |  | Name of the attribute |
| 8 | `ATTRIB_NAME_KEY` | VARCHAR(250) |  |  | Name of the attribute. This attribute name is all in capitols without punctuation. This will be used in indexing and searching of attributes by name. |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `COLUMN_NAME` | DOUBLE |  |  | Identifies a column name on the Millennium table from where to get the data for an attribute. |
| 11 | `CONTROL_GRP_CD` | DOUBLE | NOT NULL |  | Code value related to the information group (e.g. Patient Info, Encounter Info, Provider Info etc.) to which an attribute belongs. Defines a group of attributes by some common factor. |
| 12 | `CONTROL_NBR` | DOUBLE |  |  | Unique defined number for internal data processing in ProFit. |
| 13 | `CONTROL_SUB_GRP_CD` | DOUBLE | NOT NULL |  | Further defines the Attrib Control Group codeset. |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `GET_SCRIPT_NAME` | VARCHAR(30) |  |  | Name of the get script that retrieves this attribute |
| 16 | `TABLE_NAME` | DOUBLE |  |  | Identifies name of the Millennium table from where to get the data for the attribute. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `USER_DEFINED_IND` | DOUBLE |  |  | User Defined Indicator |
| 23 | `VALUE_INDEX` | DOUBLE | NOT NULL |  | Index to the value_reply structure in the corresponding get script |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ATTRIB_FIELD_RELTN](ATTRIB_FIELD_RELTN.md) | `ATTRIB_CATALOG_ID` |
| [ATTRIB_PRIMER_VAL](ATTRIB_PRIMER_VAL.md) | `ATTRIB_CATALOG_ID` |

