# OMF_INTERFACE_ERROR

> omf_interface_error

**Description:** Logs errors from omf interfaces  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTRIBUTOR_SOURCE_CD` | DOUBLE | NOT NULL |  | This will be used to specify the primary contributor source when performing alias codification/decodification for ESI and ESO transaction processes. |
| 2 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 3 | `CONTRIBUTOR_SYSTEM_STR` | VARCHAR(100) |  |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 4 | `DATA_STR` | VARCHAR(255) |  |  | The raw data string sent in the omf interface |
| 5 | `ERROR_MSG` | VARCHAR(255) |  |  | The error message resulting from an error in the omf interface. |
| 6 | `INTERFACE_COL_DESC` | VARCHAR(100) |  |  | The column description of the field that produced an error in the omf interface. |
| 7 | `INTERFACE_DT_TM` | DATETIME |  |  | The date/time that the omf interface was executed. |
| 8 | `INTERFACE_SEQ` | VARCHAR(25) |  |  | The interface sequence of the column that resulted in an error in the omf interface. |
| 9 | `OMF_INTERFACE_ERROR_ID` | DOUBLE | NOT NULL |  | The unique identifier for the omf_interface_error table |
| 10 | `PARENT_ENTITY_ALIAS` | VARCHAR(200) |  |  | The alias value for the field that resulted in an error in the omf interface. |
| 11 | `PARENT_ENTITY_ALIAS_TYPE` | VARCHAR(50) |  |  | The alias type of the field that resulted in an error in the omf interface. |
| 12 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Column no longer used. The unique identifier of the field that resulted in an error in the omf interface |
| 13 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | Column no longer used. The table name for the column value that resulted in an error in the omf interface. |
| 14 | `SEGMENT` | VARCHAR(25) |  |  | The segment that resulted in an error in the omf interface. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

