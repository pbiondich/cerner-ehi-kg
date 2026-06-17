# ESI_ALIAS_TRANS

> The ESI alias translation table contains information that determines which data fields from the incoming transaction will be used as alias identifiers in the HNA system.

**Description:** ESI Alias Translation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS_ENSURE_PARMS_FLAG` | DOUBLE | NOT NULL |  | This flag is used in conjunction with the PERSON_ALIAS_ENSURE_TYPE_CD and the ENCNTR_ALIAS_ENSURE_TYPE_CD on the ESI_ENSURE_PARMS table to determine which alias rows are eligible for the 'override' logic provided by these 'alias' ensure type codes. The options are eligible or not eligible (default). |
| 6 | `ALIAS_ENTITY_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | This field represents the identifier type, such as internal identifier type or alias type. The specific code set for the identifier type varies and corresponds to the alias_entity_name attribute within the same row. |
| 7 | `ALIAS_ENTITY_NAME` | VARCHAR(32) |  |  | This field represents the parent table for which the alias identifier, internal identifier or other identifier type will be created or found. |
| 8 | `ALIAS_FILTER_CD` | DOUBLE | NOT NULL |  | The filter method applied to the alias value (trim leading zeroes or trim trailing spaces and leading zeroes) before posting the alias value to the database. |
| 9 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL | FK→ | Alias pool code identifies a unique set or list of identifiers. |
| 10 | `ASSIGN_AUTHORITY_SYS_CD` | DOUBLE | NOT NULL |  | This field determines whether an alias will release an item from the hold queue. |
| 11 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 12 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL | FK→ | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 13 | `ELIGIBLE_FOR_QUERY_IND` | DOUBLE | NOT NULL |  | Indicates that this alias is eligible to be sent out for MPI queries. |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `ESI_ALIAS_FIELD_CD` | DOUBLE | NOT NULL |  | The HL7 or X12 message field containing the alias identifier (such as PID-2-External Identifier, PID-3-Internal Identifier). |
| 16 | `ESI_ALIAS_TRANS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the ESI_ALIAS_TRANS table. |
| 17 | `ESI_ALIAS_TYPE` | VARCHAR(50) |  |  | The alias type literal found in the message field containing the alias identifier. When valued it will be used to assist in identifying the alias row that defines the alias pool code and other processing options. For example in PID-3, the 5th component of the CX data type contains the alias type literal. |
| 18 | `ESI_ASSIGN_AUTH` | VARCHAR(50) |  |  | The assigning authority literal found in the message field containing the alias identifier. When valued it will be used to assist in identifying the alias row that defines the alias pool code and other processing options. For example in PID-3, the 4th component of the CX data type contains the assigning authority literal. When the literal is also an alias to an assigning authority organization, the SI Manager will flex the list of alias pool codes available for selection in this row. |
| 19 | `ESI_ASSIGN_FAC` | VARCHAR(50) |  |  | The place or location identifier where the identifier was first assigned to the patient. This component is not an inherent part of the identifier, but rather a part of the history of the identifier. |
| 20 | `ESI_SOURCE` | VARCHAR(50) |  |  | The personnel source literal found in the message field containing the personnel identifier. It is used to represent the personnel type and/or source. When valued it will be used to assist in identifying the alias row that defines the alias pool code and other processing options. When the literal is also an alias to an assigning authority organization, the SI Manager will flex the list of alias pool codes available for selection in this row. |
| 21 | `PERSON_PROC_OPT_CD` | DOUBLE | NOT NULL |  | Options for processing person information via ESI. |
| 22 | `PRSNL_FT_STRING` | VARCHAR(50) |  |  | The specified alias value that identifies this personnel as free-text, such as '99999'. |
| 23 | `PRSNL_PROC_OPT_CD` | DOUBLE | NOT NULL |  | This option defines how and when the interface will match existing personnel, create new 'add on the fly' personnel, and insert personnel relationship rows. |
| 24 | `SKIP_STRING` | VARCHAR(100) |  |  | A specified alias value to ignore during processing. |
| 25 | `TRUNC_SIZE` | DOUBLE |  |  | The number of characters of the alias field that remain after truncation, but before any alias filters are applied. For example, 000444 becomes 0004 when the trunc_size = 4. This is not a recommended option. Also used for the Pharmacy IVR prescription validation when the alias filter is First or Last. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALIAS_POOL_CD` | [ALIAS_POOL](ALIAS_POOL.md) | `ALIAS_POOL_CD` |
| `CONTRIBUTOR_SYSTEM_CD` | [CONTRIBUTOR_SYSTEM](CONTRIBUTOR_SYSTEM.md) | `CONTRIBUTOR_SYSTEM_CD` |

