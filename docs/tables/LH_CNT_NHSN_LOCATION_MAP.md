# LH_CNT_NHSN_LOCATION_MAP

> This table will hold the mapping between NHSN assigned nursing units identifier and organization to which it belongs to

**Description:** NHSN LOCATION MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CDC_LOCATION_LABEL_CD` | DOUBLE | NOT NULL |  | CDC Location Label defined by the CDC. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `FACILITY_CD` | DOUBLE | NOT NULL |  | Code Value of the facility. |
| 6 | `FACILITY_OID` | VARCHAR(200) | NOT NULL |  | User defined value for a facility. |
| 7 | `LH_CNT_NHSN_LOCATION_MAP_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_NHSN_LOCATION_MAP table. |
| 8 | `NHSN_UNIT_DISP_NAME` | VARCHAR(200) | NOT NULL |  | The textual display of either an facility or nursing unit. |
| 9 | `NURSE_LOC_CD` | DOUBLE | NOT NULL |  | Code Value of the nursing unit. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

