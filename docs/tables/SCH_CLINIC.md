# SCH_CLINIC

> SCHEDULING CLINIC DATA

**Description:** SCHEDULING CLINIC  
**Table type:** REFERENCE  
**Primary key:** `SCH_CLINIC_ID`  
**Columns:** 16  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CLINIC_DESCRIPTION` | VARCHAR(200) | NOT NULL |  | FREE TEXT FIELD DESCRIBING THE CLINIC |
| 4 | `CLINIC_NAME` | VARCHAR(200) | NOT NULL |  | THE NAME OF THE CLINIC |
| 5 | `CLINIC_NAME_KEY` | VARCHAR(200) | NOT NULL |  | Clinic's name all capitals with punctuation removed. this field is used for indexing and searching for a person by name. |
| 6 | `CLINIC_NAME_KEY_A_NLS` | VARCHAR(800) | NOT NULL |  | for national language support only |
| 7 | `DAYS_OF_WEEK` | VARCHAR(7) | NOT NULL |  | A character string used to store the valid days of the week. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The field identifies the current location of the clinic. |
| 10 | `ORIG_SCH_CLINIC_ID` | DOUBLE | NOT NULL | FK→ | ORIGINAL SCH_CLINIC_ID for this set of versioned entries. Required for Type-2 Versioning |
| 11 | `SCH_CLINIC_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORIG_SCH_CLINIC_ID` | [SCH_CLINIC](SCH_CLINIC.md) | `SCH_CLINIC_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [SCH_CLINIC](SCH_CLINIC.md) | `ORIG_SCH_CLINIC_ID` |
| [SCH_CLINIC_PRSNL_RELTN](SCH_CLINIC_PRSNL_RELTN.md) | `SCH_CLINIC_ID` |
| [SCH_CLINIC_RELTN](SCH_CLINIC_RELTN.md) | `SCH_CLINIC_ID` |
| [SCH_DEF_APPLY](SCH_DEF_APPLY.md) | `SCH_CLINIC_ID` |
| [SCH_LOCATION](SCH_LOCATION.md) | `SCH_CLINIC_ID` |

