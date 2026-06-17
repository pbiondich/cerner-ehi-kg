# SI_SERVICE_RELTN

> Relates entities like Contributor Systems and OIDs to Services

**Description:** System Integration Service Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTHORIZATION_TYPE_CD` | DOUBLE | NOT NULL |  | Authorization Type Code |
| 2 | `AUTH_LOCATION_URI` | VARCHAR(255) |  |  | Location of the Authorization Uniform Resource Identifier |
| 3 | `CERTIFICATE_LOCATION_URI` | VARCHAR(255) |  |  | Location of the Certificate Uniform Resource Identifier |
| 4 | `CERTIFICATE_TYPE_CD` | DOUBLE | NOT NULL |  | Certificate Type Code |
| 5 | `CONTENT_CAT_FILTER_CD` | DOUBLE | NOT NULL |  | Optional value used to filter services to used based on the content category of the service request. |
| 6 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | Indicates that this row is the default reltn to use based on the external_service_type_cd, parent_entity_name, parent_entity_id, and content_cat_filter_cd values |
| 7 | `EXTERNAL_SERVICE_TYPE_CD` | DOUBLE | NOT NULL |  | The type of service utilized for this system. |
| 8 | `LISTENER_ALIAS` | VARCHAR(48) |  |  | The selected Listener Alias used for processing as it relates to the External Service. |
| 9 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The primary key of the entity table related to the service. |
| 10 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The name of the entity that will relate to the service in question. This value can be CONTRIBUTOR_SYSTEM, LOCATION, ORGANIZATION, or SI_OID. |
| 11 | `SERVICE_URI` | VARCHAR(512) |  |  | Location of the Service Uniform Resource Identifier |
| 12 | `SI_EXTERNAL_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Number that identifies a single row on the SI_EXTERNAL_SERVICE table |
| 13 | `SI_SERVICE_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the SI_SERVICE_RELTN table. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SI_EXTERNAL_SERVICE_ID` | [SI_EXTERNAL_SERVICE](SI_EXTERNAL_SERVICE.md) | `SI_EXTERNAL_SERVICE_ID` |

