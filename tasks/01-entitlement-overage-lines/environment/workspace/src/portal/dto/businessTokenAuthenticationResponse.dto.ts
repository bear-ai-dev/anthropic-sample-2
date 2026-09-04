import { ApiProperty } from '@nestjs/swagger';

export class BusinessTokenAuthenticationResponse {
    /***
     * A JWT authentication token which can be used to securely share selected business data with external parties.
     * <br><br>
     *
     * @example "[REDACTED JWT]"
     */
    @ApiProperty({ externalDocs: { description: 'Read more about JWTs', url: 'https://jwt.io/introduction/' } })
    public access_token: string;
}
