# SI_OID

> This table will store OID information for use in determining code systems for outbound aliases and identifiers.

**Description:** System Integration Object Identifier  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CERNER_DEFINED_IND` | DOUBLE | NOT NULL |  | If this field is set to 1 then this is a pre-populated OID that has been certified by Cerner and shouldn't be modified by the client. |
| 4 | `CONTRIBUTOR_SOURCE_CD` | DOUBLE | NOT NULL |  | This is a contributor_source_cd that is related to the OID, it is not required. In some cases it is used as part of the select, in others it is sent back to the calling object for additional functionality. This is based on the type of OID selected. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `ENTITY_ID` | DOUBLE | NOT NULL |  | A numeric identifier that is related to the Parent Entity Name to define the OID. This field can store values form Code Set 400 or 263. It isn't required depending upon the type of OID. |
| 7 | `ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Parent Table Name related to the ENTITY_ID value if ENTITY_ID is not zero. |
| 8 | `ENTITY_TYPE` | VARCHAR(40) | NOT NULL |  | A String description of the type of OID being stored, possible options are ALIASPOOL, ALLERGYID, NOMENCLATURE, ADMINISTRATIVEGENDER. This field is required with ENTITY_ID is zero. |
| 9 | `OID_DISPLAY` | VARCHAR(100) |  |  | Human readable display of the oid text |
| 10 | `OID_TXT` | VARCHAR(200) | NOT NULL |  | The OID for the Code System related to the given Parent Entity Name/ID. This should be in for of an OID #.#.# |
| 11 | `SI_OID_ID` | DOUBLE | NOT NULL |  | Unique Identifier for the SI_OID table. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

