# ENCNTR_PERSON_RELTN

> The encounter-person relationship table contains pointers to related persons in the person table .The kind of relationship (i.e., accompanied by, accident witness, etc.) and genetic indication defines how the encounter and person are related.

**Description:** Encounter Person Relationship  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_PERSON_RELTN_ID`  
**Columns:** 34  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CONTACT_ROLE_CD` | DOUBLE | NOT NULL |  | This field is equivalent to the HL7 contact role field in the Next of Kin segment. This field is generally not used by the Cerner system, since there are other preferred ways to store data indicated by this HL7 field. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `COPY_CORRESPONDENCE_CD` | DOUBLE | NOT NULL |  | Denotes whether the related person should be copied on any correspondence to the person. |
| 9 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 10 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 11 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 12 | `DEFAULT_RELTN_IND` | DOUBLE |  |  | Identifies whether the relationship is the default displayable Mother-Child relationship. |
| 13 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 14 | `ENCNTR_PERSON_RELTN_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the encounter person relationship table. It is an internal system assigned number. |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `FAMILY_RELTN_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | The specific family relationship |
| 17 | `FREE_TEXT_CD` | DOUBLE | NOT NULL |  | Describes the type of free text information that is available for the person. When set to a meaning of 'FTBRIEF', this indicates that the related_person_id is NULL, meaning that there is no reference to the person table. |
| 18 | `FT_REL_PERSON_NAME` | VARCHAR(100) |  |  | The name of the person in the 'free text' relationship indicated by the free_text_ind in the row being set to 'TRUE'. |
| 19 | `GENETIC_RELATIONSHIP_IND` | DOUBLE | NOT NULL |  | Indicates whether the relationship is genetic. |
| 20 | `INTERNAL_SEQ` | DOUBLE | NOT NULL |  | Sequence used within Cerner applications to order encounter person relationship rows. |
| 21 | `LIVING_WITH_IND` | DOUBLE | NOT NULL |  | Indicates whether the encounter's person (patient) is living with the person represented by the related_person_id. |
| 22 | `PERSON_RELTN_CD` | DOUBLE | NOT NULL |  | Identifies the specific type of relationship between two persons for the encounter. This field is user defined (I.e., father, mother, spouse, self, friend, etc.). This is equivalent to the HL7 relationship field in the Next of Kin segment. |
| 23 | `PERSON_RELTN_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the general type of relationship between two persons for the encounter. This field is has meanings in the common data foundation which are defined by Cerner (I.e., next of kin, emergency contact, default guarantor, etc.) |
| 24 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Identifies an sequencing priority to be used when there is more than one related person with the same person relationship type (I.e., emergency contact) |
| 25 | `RELATED_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. This is a 'role' name for the reference to person_id in the person table and used to differentiate between other references to person_id in this table. |
| 26 | `RELATED_PERSON_RELTN_CD` | DOUBLE | NOT NULL |  | This identifies the inverse specific relationship of the two person for the encounter. |
| 27 | `RELATION_SEQ` | DOUBLE | NOT NULL |  | Zero based sequence for all encntr_ person_reltn rows across all relation types set by the master system. Added to support he UK's PDS transactions. |
| 28 | `SOURCE_IDENTIFIER` | VARCHAR(255) |  |  | Identifier assigned from a master system to this row. Added to support he UK's PDS Allocated Object Identifier. Used to help keep the UK master database in sync with Millennium. |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 34 | `VISITATION_ALLOWED_CD` | DOUBLE | NOT NULL |  | Identifies whether or not the related person has visitation privilege, potentially specifying the level of privilege. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `RELATED_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ENCNTR_PERSON_RELTN_HIST](ENCNTR_PERSON_RELTN_HIST.md) | `ENCNTR_PERSON_RELTN_ID` |

