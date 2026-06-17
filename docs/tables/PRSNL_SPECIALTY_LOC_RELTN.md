# PRSNL_SPECIALTY_LOC_RELTN

> Defines a relationship between personnel specialties and a location

**Description:** Personnel Specialty Location Relationship  
**Table type:** REFERENCE  
**Primary key:** `PRSNL_SPECIALTY_LOC_RELTN_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Contains the value of the related location for this relationship. |
| 5 | `ORIG_PRSNL_SPECIALTY_LOC_R_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of the personnel location relationship. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 6 | `PRSNL_SPECIALTY_LOC_RELTN_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a relationship between a personnel and a provider specialty location. Unique generated number that identifies a single row on the prsnl_specialty_loc_reltn table. |
| 7 | `PRSNL_SPECIALTY_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies thepersonnel to specialty relationship. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORIG_PRSNL_SPECIALTY_LOC_R_ID` | [PRSNL_SPECIALTY_LOC_RELTN](PRSNL_SPECIALTY_LOC_RELTN.md) | `PRSNL_SPECIALTY_LOC_RELTN_ID` |
| `PRSNL_SPECIALTY_RELTN_ID` | [PRSNL_SPECIALTY_RELTN](PRSNL_SPECIALTY_RELTN.md) | `PRSNL_SPECIALTY_RELTN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PRSNL_SPECIALTY_LOC_RELTN](PRSNL_SPECIALTY_LOC_RELTN.md) | `ORIG_PRSNL_SPECIALTY_LOC_R_ID` |

